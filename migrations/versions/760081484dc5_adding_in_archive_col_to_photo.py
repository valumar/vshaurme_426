"""Adding in_archive col to Photo

Revision ID: 760081484dc5
Revises: 050788f423a5
Create Date: 2019-06-12 21:46:24.933698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '760081484dc5'
down_revision = '050788f423a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('in_archive', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.drop_column('in_archive')

    # ### end Alembic commands ###
