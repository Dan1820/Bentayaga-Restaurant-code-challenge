class Customer:
    all_customers = []

    def _init_(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        self.all_customers.append(self)

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        self._given_name = given_name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        self._family_name = family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def restaurants(self):
        unique_restaurants = []
        for review in self.reviews:
            restaurant = review.restaurant
            if restaurant not in unique_restaurants:
                unique_restaurants.append(restaurant)
        return unique_restaurants

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                customers.append(customer)
        return customers

    @classmethod
    def all(cls):
        return cls.all_customers
    
class Restaurant:
    all_restaurants = []

    def _init_(self, name):
        self._name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    def restaurant_reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = []
        for review in self.reviews:
            customer = review.customer
            if customer not in unique_customers:
                unique_customers.append(customer)
        return unique_customers

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0

    @classmethod
    def all(cls):
        return cls.all_restaurants
    
class Review:
    all_reviews = []

    def _init_(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews
    

customer1= Customer("duncan","kipkemoi")
# customer2=Customer('Diana ', 'Kyalo')
# customer3=Customer("Dennis","Mwanza")
# customer4=Customer('Kennedy','Kiplangat')
restaurant=Restaurant('pizza inn')
customer1.add_review(restaurant,5)
customer1.add_review(restaurant,5)
customer1.add_review(restaurant,5)
# customer2.add_review(restaurant,4)
# customer3.add_review(restaurant,3)
# customer4.add_review(restaurant,2)

# print(customer1.num_of_reviews())

# print(all_customers)