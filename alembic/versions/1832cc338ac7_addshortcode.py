"""addshortcode

Revision ID: 1832cc338ac7
Revises: ad22ddf35f06
Create Date: 2022-05-22 17:12:08.267067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1832cc338ac7'
down_revision = 'ad22ddf35f06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parties', sa.Column('short_code', sa.String(), nullable=True))
    op.create_index(op.f('ix_parties_short_code'), 'parties', ['short_code'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_parties_short_code'), table_name='parties')
    op.drop_column('parties', 'short_code')
    # ### end Alembic commands ###
