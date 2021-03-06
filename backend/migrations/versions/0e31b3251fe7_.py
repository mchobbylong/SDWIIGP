"""empty message

Revision ID: 0e31b3251fe7
Revises: d65619966782
Create Date: 2019-05-18 22:47:40.769537

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e31b3251fe7'
down_revision = 'd65619966782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar', sa.String(length=256), server_default='default.jpg', nullable=False))
    op.drop_column('user', 'photo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('photo', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('user', 'avatar')
    # ### end Alembic commands ###
