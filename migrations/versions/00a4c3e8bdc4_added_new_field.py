"""added new field

Revision ID: 00a4c3e8bdc4
Revises: 4fa47ac8c205
Create Date: 2021-04-28 07:25:41.948120

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '00a4c3e8bdc4'
down_revision = '4fa47ac8c205'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('test', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'test')
    # ### end Alembic commands ###
