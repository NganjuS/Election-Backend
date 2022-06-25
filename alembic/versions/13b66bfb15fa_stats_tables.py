"""stats tables

Revision ID: 13b66bfb15fa
Revises: d9282ea5a5b3
Create Date: 2022-06-23 21:40:45.684209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b66bfb15fa'
down_revision = 'd9282ea5a5b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('statsdata_statsbatch_id_fkey', 'statsdata', type_='foreignkey')
    op.drop_column('statsdata', 'statsbatch_id')
    op.add_column('statsources', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statsources', 'website')
    op.add_column('statsdata', sa.Column('statsbatch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('statsdata_statsbatch_id_fkey', 'statsdata', 'statsbatch', ['statsbatch_id'], ['id'])
    # ### end Alembic commands ###
