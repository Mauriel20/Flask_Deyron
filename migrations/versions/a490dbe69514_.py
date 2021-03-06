"""empty message

Revision ID: a490dbe69514
Revises: 762402052503
Create Date: 2021-03-30 21:11:57.450756

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a490dbe69514'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paciente',
    sa.Column('DNI', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('suffering', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('DNI')
    )
    op.create_table('hospital',
    sa.Column('DNI_cita', sa.Integer(), nullable=False),
    sa.Column('birth', sa.String(length=250), nullable=False),
    sa.Column('Hora', sa.Integer(), nullable=False),
    sa.Column('DNI_paciente_hospital', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['DNI_paciente_hospital'], ['paciente.DNI'], ),
    sa.PrimaryKeyConstraint('DNI_cita')
    )
    op.drop_index('email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`is_active` in (0,1))', name='user_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('hospital')
    op.drop_table('paciente')
    # ### end Alembic commands ###
