from config import Base, engine

from database.init_db_data import (initialize_materials, initialize_product_type, initialize_products, initialize_partners,
                                   initialize_orders)

Base.metadata.create_all(engine)

initialize_materials()
initialize_product_type()
initialize_products()
initialize_partners()
initialize_orders()