from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from forms import SectorForm, ObjectsForm, Natural_objectsForm, PositionForm, RelationsForm
from models import db, Sector, Objects, NaturalObjects, Position, Relations
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost/SpaceObservations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db.init_app(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

@app.route('/')
def index():
    sectors = Sector.query.all()
    objects = Objects.query.all()
    natural_objects = NaturalObjects.query.all()
    positions = Position.query.all()
    relations = Relations.query.all()
    return render_template('index.html', sectors=sectors, objects=objects, natural_objects=natural_objects, positions=positions, relations=relations)

# Generic route to add entities
@app.route('/add_<entity>', methods=['GET', 'POST'])
def add_entity(entity):
    form_class = globals().get(f'{entity.capitalize()}Form')
    if not form_class:
        flash(f'Form for entity {entity} not found', 'danger')
        return redirect(url_for('index'))
    
    form = form_class()
    if form.validate_on_submit():
        new_entity = globals()[entity.capitalize()]()
        form.populate_obj(new_entity)
        db.session.add(new_entity)
        try:
            db.session.commit()
            flash(f'{entity.capitalize()} added successfully!', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error adding {entity}: {str(e)}', 'danger')
        return redirect(url_for('index'))
    return render_template('add.html', form=form, entity_name=entity.capitalize(), action='add')

# Generic route to edit entities
@app.route('/edit_<entity>/<int:id>', methods=['GET', 'POST'])
def edit_entity(entity, id):
    entity_class = globals()[entity.capitalize()]
    entity_instance = entity_class.query.get_or_404(id)
    form = globals()[f'{entity.capitalize()}Form'](obj=entity_instance)
    if form.validate_on_submit():
        for field in form:
            setattr(entity_instance, field.name, field.data)
        try:
            db.session.commit()
            flash(f'{entity.capitalize()} updated successfully!', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Error updating {entity}: {str(e)}', 'danger')
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, entity_name=entity.capitalize(), action='edit')

# Generic route to delete entities
@app.route('/delete_<entity>/<int:id>', methods=['GET', 'POST'])
def delete_entity(entity, id):
    entity_class = globals()[entity.capitalize()]
    entity_instance = entity_class.query.get_or_404(id)
    db.session.delete(entity_instance)
    try:
        db.session.commit()
        flash(f'{entity.capitalize()} deleted successfully!', 'success')
    except IntegrityError as e:
        db.session.rollback()
        flash(f'Error deleting {entity}: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/jointables')
def join_tables():
    connection = engine.raw_connection()
    try:
        cursor = connection.cursor()
        cursor.callproc('JoinSectorAndObjects')
        for result in cursor.stored_results():
            results = result.fetchall()
        cursor.close()
    finally:
        connection.close()
    
    return render_template('jointables.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
