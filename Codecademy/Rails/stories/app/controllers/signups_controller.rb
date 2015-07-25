class SignupsController < ApplicationController
	def new
		@signup = Signup.new
	end

  	def create 
  		@signup = Signup.new(signup_params) 
  		if @signup.save 
    		#ThanksMailer.thanks.deliver_now
    		redirect_to '/thanks' 
  		else 
    		render 'new' 
  		end 
	end

	def thanks
		@signup = Signup.last
	end

	private
		def signup_params
			params.require(:signup).permit(:email, :firstname)
		end
end
