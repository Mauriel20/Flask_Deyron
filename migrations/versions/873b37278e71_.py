"""empty message

Revision ID: 873b37278e71
Revises: 5c27b6504623
Create Date: 2021-03-31 01:10:02.323508

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '873b37278e71'
down_revision = '5c27b6504623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hospital', sa.Column('birth', sa.DATETIME(), nullable=True))
    op.drop_column('hospital', 'Fecha')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hospital', sa.Column('Fecha', mysql.DATETIME(), nullable=True))
    op.drop_column('hospital', 'birth')
    # ### end Alembic commands ###
