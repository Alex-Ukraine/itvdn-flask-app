"""added new field

Revision ID: 00a4c3e8bdc4
Revises: 4fa47ac8c205
Create Date: 2021-04-28 07:25:41.948120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = '00a4c3e8bdc5'
down_revision = '00a4c3e8bdc4'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%Deathly%'
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%Deathly%'
            """
        )
    )
