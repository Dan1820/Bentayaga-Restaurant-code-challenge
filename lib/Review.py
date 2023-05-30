class Review:
    reviews=[]

    def __init__(self,customer,restaurant,rating):
        self.customer=customer
        self.restaurant=restaurant
        self.rating=rating
        self.reviews.append(self)

    def review_rating(self):
        return self.rating
    

    @classmethod
    def all_reviews(cls):
        return cls.reviews
    
    def customer_review(self):
        return self.customer
    
    def restaurant_review(self):
        return self.restaurant
