#Using a predicate 'be' matcher, make sure that a tweet like "Nom nom nom" (which is not a reply because it doesn't start with an '@' sign) is public.

describe Tweet do
  it 'without a leading @ symbol should be public' do
    tweet = Tweet.new(status: 'Nom nom nom')
    tweet.should be_public
  end
end
