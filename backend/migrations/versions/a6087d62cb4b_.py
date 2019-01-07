"""empty message

Revision ID: a6087d62cb4b
Revises: 3699cb98fc2a
Create Date: 2018-12-10 11:38:36.875419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6087d62cb4b'
down_revision = '3699cb98fc2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=255), nullable=False))
    op.alter_column('user', 'email_address',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_constraint('user_account_address_key', 'user', type_='unique')
    op.drop_column('user', 'account_address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('account_address', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_account_address_key', 'user', ['account_address'])
    op.alter_column('user', 'email_address',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###