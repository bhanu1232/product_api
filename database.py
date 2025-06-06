from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, func
from datetime import datetime
import os

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False, index=True)
    discount_percentage = db.Column(db.Float, default=0)
    rating = db.Column(db.Float, default=0, index=True)
    stock = db.Column(db.Integer, default=0, index=True)
    brand = db.Column(db.String(100), nullable=False, index=True)
    category = db.Column(db.String(100), nullable=False, index=True)
    thumbnail = db.Column(db.String(500))
    images = db.Column(db.Text)  # JSON string of image URLs
    sku = db.Column(db.String(50), unique=True)
    weight = db.Column(db.Float)
    dimensions = db.Column(db.String(100))
    warranty_information = db.Column(db.String(200))
    shipping_information = db.Column(db.String(200))
    availability_status = db.Column(db.String(50), default='In Stock')
    return_policy = db.Column(db.String(200))
    minimum_order_quantity = db.Column(db.Integer, default=1)
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.String(500))
    meta_keywords = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'discountPercentage': self.discount_percentage,
            'rating': self.rating,
            'stock': self.stock,
            'brand': self.brand,
            'category': self.category,
            'thumbnail': self.thumbnail,
            'images': eval(self.images) if self.images else [],
            'sku': self.sku,
            'weight': self.weight,
            'dimensions': self.dimensions,
            'warrantyInformation': self.warranty_information,
            'shippingInformation': self.shipping_information,
            'availabilityStatus': self.availability_status,
            'returnPolicy': self.return_policy,
            'minimumOrderQuantity': self.minimum_order_quantity,
            'meta': {
                'title': self.meta_title,
                'description': self.meta_description,
                'keywords': self.meta_keywords
            },
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def search(cls, query, category=None, min_price=None, max_price=None, brand=None, in_stock=None):
        """Advanced search functionality"""
        search_query = cls.query
        
        # Text search across multiple fields
        if query:
            search_terms = query.lower().split()
            conditions = []
            for term in search_terms:
                term_conditions = or_(
                    cls.title.ilike(f'%{term}%'),
                    cls.description.ilike(f'%{term}%'),
                    cls.brand.ilike(f'%{term}%'),
                    cls.category.ilike(f'%{term}%'),
                    cls.sku.ilike(f'%{term}%')
                )
                conditions.append(term_conditions)
            
            if conditions:
                search_query = search_query.filter(and_(*conditions))
        
        # Category filter
        if category:
            search_query = search_query.filter(cls.category.ilike(f'%{category}%'))
        
        # Price range filter
        if min_price is not None:
            search_query = search_query.filter(cls.price >= min_price)
        if max_price is not None:
            search_query = search_query.filter(cls.price <= max_price)
        
        # Brand filter
        if brand:
            search_query = search_query.filter(cls.brand.ilike(f'%{brand}%'))
        
        # Stock filter
        if in_stock:
            search_query = search_query.filter(cls.stock > 0)
        
        return search_query
    
    @classmethod
    def get_categories(cls):
        """Get all unique categories"""
        return [cat[0] for cat in db.session.query(cls.category.distinct()).all()]
    
    @classmethod
    def get_brands(cls):
        """Get all unique brands"""
        return [brand[0] for brand in db.session.query(cls.brand.distinct()).all()]

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'parent_id': self.parent_id
        }
