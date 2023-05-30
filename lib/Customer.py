class Customer:
    customers=[]
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.reviews=[]
        self.customers.append(self)

    # def first_name(self):
    #     return self._first_name
    
    # def customer_last_name(self):
    #     return self.last_name
    

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

    @classmethod
    def all(cls):
        return cls.customers
    

    #return the total reviews
    def num_of_reviews(self):
        return len(self.reviews)
    

    #aggregation and association
    #finds the names of the customers
    @classmethod
    def find_by_name(cls,name):
        for customer in cls.customers:
            if customer.full_name()==name:
                return customer
            return None
        
    #return a list of all the  customers
    @classmethod
    def find_all_by_name(cls,name):
        customer_name_available=[]
        for customer in cls.customers:
            if customer.first_name==name:
                customer_name_available.append(customer)
                return customer_name_available
            
    def add_review(self,restaurant,rating):
        review= Review(self,restaurant,rating)
        self.reviews.append(review)


class Restaurant:
    def __init__(self,name):
        self.name=name
        self.reviews=[]
    
    def restaurant_name(self):
        return self.name
    
    def average_star_rating(self):
        if len(self.reviews)==0:
            return 0
        total_rating=0
        for review in self.reviews:
            total_rating += review.rating 
        return total_rating/len(self.reviews)
    def restaurant_reviews(self):
        return self.reviews
    def customers(self):
        return list(set(review.customer for review in self.reviews))
    
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


customer1= Customer("duncan","kipkemoi")
customer2=Customer('Diana ', 'Kyalo')
customer3=Customer("Dennis","Mwanza")
customer4=Customer('Kennedy','Kiplangat')
restaurant=Restaurant('pizza inn')
customer1.add_review(restaurant,5)
customer1.add_review(restaurant,5)
customer1.add_review(restaurant,5)
customer2.add_review(restaurant,4)
customer3.add_review(restaurant,3)
customer4.add_review(restaurant,2)

# print(customer1.num_of_reviews())

# print(Customer.find_by_name(customer1))

# print(restaurant.average_star_rating())
print(restaurant.customers())


            
        

            
        

