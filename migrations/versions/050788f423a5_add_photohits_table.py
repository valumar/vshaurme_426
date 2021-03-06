"""Add PhotoHits table

Revision ID: 050788f423a5
Revises: 
Create Date: 2019-06-09 20:23:09.874539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050788f423a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_hits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('photo_hits', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_photo_hits_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo_hits', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_photo_hits_timestamp'))

    op.drop_table('photo_hits')
    # ### end Alembic commands ###
