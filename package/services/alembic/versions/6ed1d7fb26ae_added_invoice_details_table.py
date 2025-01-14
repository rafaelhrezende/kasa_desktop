"""Added invoice_details table

Revision ID: 6ed1d7fb26ae
Revises: a6fd473eabf6
Create Date: 2023-09-03 12:18:50.687776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ed1d7fb26ae'
down_revision = 'a6fd473eabf6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('value', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('locale_description', sa.String(length=300), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_invoice_details_id'), 'invoice_details', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invoice_details_id'), table_name='invoice_details')
    op.drop_table('invoice_details')
    # ### end Alembic commands ###
