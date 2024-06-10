from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, DateTimeField, DateField, TimeField
from wtforms.validators import DataRequired

class SectorForm(FlaskForm):
    class Meta:
        csrf = False
    coordinates = StringField('Coordinates', validators=[DataRequired()])
    light_intensity = FloatField('Light Intensity', validators=[DataRequired()])
    foreign_objects = TextAreaField('Foreign Objects')
    num_sky_objects = IntegerField('Number of Sky Objects', validators=[DataRequired()])
    num_undefined_objects = IntegerField('Number of Undefined Objects', validators=[DataRequired()])
    num_defined_objects = IntegerField('Number of Defined Objects', validators=[DataRequired()])
    notes = TextAreaField('Notes')

class ObjectsForm(FlaskForm):
    class Meta:
        csrf = False
    type = StringField('Type', validators=[DataRequired()])
    determination_accuracy = FloatField('Determination Accuracy', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    note = TextAreaField('Note')

class Natural_objectsForm(FlaskForm):
    class Meta:
        csrf = False
    type = StringField('Type', validators=[DataRequired()])
    galaxy = StringField('Galaxy', validators=[DataRequired()])
    accuracy = FloatField('Accuracy', validators=[DataRequired()])
    light_flow = FloatField('Light Flow', validators=[DataRequired()])
    coupled_objects = TextAreaField('Coupled Objects')
    note = TextAreaField('Note')

class PositionForm(FlaskForm):
    class Meta:
        csrf = False
    earth_position = StringField('Earth Position', validators=[DataRequired()])
    sun_position = StringField('Sun Position', validators=[DataRequired()])
    moon_position = StringField('Moon Position', validators=[DataRequired()])

class RelationsForm(FlaskForm):
    class Meta:
        csrf = False
    sector_id = IntegerField('Sector ID', validators=[DataRequired()])
    object_id = IntegerField('Object ID', validators=[DataRequired()])
    natural_object_id = IntegerField('Natural Object ID', validators=[DataRequired()])
    position_id = IntegerField('Position ID', validators=[DataRequired()])
