"""empty message

Revision ID: 31eec8f1a8ee
Revises: 
Create Date: 2021-12-05 19:14:30.859728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31eec8f1a8ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('uid', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('site',
    sa.Column('uid', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('max_power', sa.Float(), nullable=False),
    sa.Column('manager_id', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['manager.uid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('asset',
    sa.Column('uid', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('power', sa.Float(), nullable=False),
    sa.Column('asset_type', sa.String(length=100), nullable=False),
    sa.Column('site_id', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['site_id'], ['site.uid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('asset')
    op.drop_table('site')
    op.drop_table('manager')
    # ### end Alembic commands ###
