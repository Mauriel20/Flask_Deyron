"""empty message

Revision ID: a80cd22104ad
Revises: b605ff6161a2
Create Date: 2021-03-30 23:53:02.016711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a80cd22104ad'
down_revision = 'b605ff6161a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hospital', sa.Column('Fecha', sa.DATETIME(), nullable=True))
    op.drop_column('hospital', 'Hora')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hospital', sa.Column('Hora', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('hospital', 'Fecha')
    # ### end Alembic commands ###