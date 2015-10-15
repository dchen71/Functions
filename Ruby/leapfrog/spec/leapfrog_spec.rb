require_relative "../leapfrog"
require 'rspec'

describe Leapfrog do
  subject(:leapfrog) { Leapfrog.new(10,85,30) }

  it "has accessor for x" do
    is_expected.to respond_to(:x) 
  end 
  it "has accessor for y" do
    is_expected.to respond_to(:y) 
  end
  it "has accessor for d" do
    is_expected.to respond_to(:d) 
  end
  it "has accessor for jumps" do
    is_expected.to respond_to(:jumps) 
  end
  it "has method calc_jumps" do
    is_expected.to respond_to(:calc_jumps) 
  end
  context "values" do
  it "content attribute should have value \"test\"" do
    expect(leapfrog.calc_jumps).to eq(3)
  end
end
end