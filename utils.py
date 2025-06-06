import math

def paginate_results(items, skip, limit):
    """Paginate a list of items"""
    start = skip
    end = skip + limit
    return items[start:end]

def search_products(products, query):
    """Search products by title, description, brand, or category"""
    query = query.lower()
    results = []
    
    for product in products:
        if (query in product.title.lower() or 
            query in product.description.lower() or 
            query in product.brand.lower() or 
            query in product.category.lower()):
            results.append(product)
    
    return results

def filter_by_category(products, category):
    """Filter products by category"""
    return [product for product in products if product.category.lower() == category.lower()]

def sort_products(products, sort_by, order='asc'):
    """Sort products by a specific field"""
    reverse = order.lower() == 'desc'
    
    try:
        if sort_by in ['price', 'rating', 'discountPercentage', 'stock']:
            return sorted(products, key=lambda x: getattr(x, sort_by), reverse=reverse)
        elif sort_by in ['title', 'brand', 'category']:
            return sorted(products, key=lambda x: getattr(x, sort_by).lower(), reverse=reverse)
        else:
            return products
    except AttributeError:
        return products
