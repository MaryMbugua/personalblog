"""migrate again

Revision ID: c198a100215b
Revises: a261b0c1e51b
Create Date: 2018-02-15 08:41:40.065096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c198a100215b'
down_revision = 'a261b0c1e51b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('fake_date', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogposts', 'fake_date')
    # ### end Alembic commands ###
