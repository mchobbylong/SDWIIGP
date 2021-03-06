"""empty message

Revision ID: 9d2704ae7566
Revises: cb362fb020f4
Create Date: 2019-05-19 04:23:36.949342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d2704ae7566'
down_revision = 'cb362fb020f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('task_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'submission', 'task', ['task_id'], ['task_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_column('submission', 'task_id')
    # ### end Alembic commands ###
