class Signup < ActiveRecord::Base
	validates :firstname, presence: true
	validates :email, presence: true
end
