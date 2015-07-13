class ThanksMailer < ApplicationMailer
	def thanks
		@user = Signup.last
		@name = @user.firstname
		mail(to: @user.email,subject: "Thanks!Stories will be coming soon")
	end

end
