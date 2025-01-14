"""DB Init

Revision ID: a6fd473eabf6
Revises: 
Create Date: 2023-06-19 00:09:44.056597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6fd473eabf6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('initial_value', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('payment_day', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bills_description'), 'bills', ['description'], unique=False)
    op.create_index(op.f('ix_bills_id'), 'bills', ['id'], unique=False)
    op.create_index(op.f('ix_bills_title'), 'bills', ['title'], unique=False)
    op.create_table('processes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('process_key', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('start_at', sa.DateTime(), nullable=True),
    sa.Column('finish_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=25), nullable=True),
    sa.Column('observation', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_processes_id'), 'processes', ['id'], unique=False)
    op.create_table('invoices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('method', sa.String(length=50), nullable=True),
    sa.Column('reference_year', sa.Integer(), nullable=True),
    sa.Column('reference_month', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('value', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('completion_date', sa.Date(), nullable=True),
    sa.Column('pay_day', sa.Date(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('bill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bill_id'], ['bills.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_invoices_id'), 'invoices', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_invoices_id'), table_name='invoices')
    op.drop_table('invoices')
    op.drop_index(op.f('ix_processes_id'), table_name='processes')
    op.drop_table('processes')
    op.drop_index(op.f('ix_bills_title'), table_name='bills')
    op.drop_index(op.f('ix_bills_id'), table_name='bills')
    op.drop_index(op.f('ix_bills_description'), table_name='bills')
    op.drop_table('bills')
    # ### end Alembic commands ###
