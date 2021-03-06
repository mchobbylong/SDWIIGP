from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, SelectMultipleField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from flask import request
from app.model import Problem, Tag


class FormProblem(FlaskForm):
	def query_factory():
		return Tag.query.all()

	title = StringField('Title', validators=[DataRequired(message='Title is required')])
	description = TextAreaField('Description', validators=[DataRequired(message='Description is required')])
	level = SelectField('Level', coerce=int, choices=[(k, k) for k in range(1, 4)])
	tags = QuerySelectMultipleField('Tags', query_factory=query_factory)
	# tags = SelectMultipleField('Tags', coerce=int, choices=[(k, k) for k in range(1, 4)])
	submit = SubmitField('Save')

	def __init__(self, pid, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if request.method == 'GET' and pid:
			problem = Problem.query.filter_by(pid = pid).first()
			self.title.data = problem.title
			self.description.data = problem.description
			self.level.data = problem.level
			self.tags.data = problem.tags.all()

class FormProblemFilter(FlaskForm):
	level = SelectField('Level', choices = [('0', 'All levels'), ('1', '1'), ('2', '2'), ('3', '3')])
	title = StringField('Problem Title')
	tag_id = StringField('tag_id')
	page = StringField('page')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level.data = request.values.get('level') or 0
		self.title.data = request.values.get('title')
		self.tag_id.data = request.values.get('tag_id')
		self.page.data = request.values.get('page') or 1

	@property
	def collapsed(self):
		return int(self.level.data) == 0 and (not self.title.data)
