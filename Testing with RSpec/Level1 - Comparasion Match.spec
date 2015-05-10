#Finish the example below to ensure that our tweet.status.length is less than or equal to 140 characters. 
#Use a be matcher in your spec

describe Tweet do
  it 'truncates the status to 140 characters' do
    tweet = Tweet.new(status: 'Nom nom nom' * 100)
    tweet.status.length.should be <=140
  end
end