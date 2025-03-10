"""empty message

Revision ID: 3bd9c19c5f3e
Revises: 841d5bb171db
Create Date: 2024-12-26 14:11:49.407671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bd9c19c5f3e'
down_revision = '841d5bb171db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('piece', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('fk_property_user', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('rent_no_set', sa.Integer(), nullable=False),
    sa.Column('rent_color_set', sa.Integer(), nullable=False),
    sa.Column('rent_1_house', sa.Integer(), nullable=False),
    sa.Column('rent_2_house', sa.Integer(), nullable=False),
    sa.Column('rent_3_house', sa.Integer(), nullable=False),
    sa.Column('rent_4_house', sa.Integer(), nullable=False),
    sa.Column('rent_hotel', sa.Integer(), nullable=False),
    sa.Column('building_cost', sa.Integer(), nullable=False),
    sa.Column('mortgage', sa.Integer(), nullable=False),
    sa.Column('unmortgage', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['fk_property_user'], ['players.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    op.drop_table('players')
    # ### end Alembic commands ###
