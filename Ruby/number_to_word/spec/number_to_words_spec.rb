require_relative '../number_to_words'

RSpec.describe "#number_to_words" do
  it "should work for 0" do
    expect(number_to_words(0)).to eq("zero")
  end

  it "should work for 1" do
    expect(number_to_words(1)).to eq("one")
  end

  it "should work for 2" do
    expect(number_to_words(2)).to eq("two")
  end

  it "should work for 10" do
    expect(number_to_words(10)).to eq("ten")
  end

  it "should work for 42" do
    expect(number_to_words(42)).to eq("forty-two")
  end

  it "should work for 200" do
    expect(number_to_words(200)).to eq("two hundred")
  end

  it "should work for 250" do
    expect(number_to_words(250)).to eq("two hundred and fifty")
  end

  it "should work for 251" do
    expect(number_to_words(251)).to eq("two hundred and fifty-one")
  end

  it "should work for 1000" do
    expect(number_to_words(1000)).to eq("one thousand")
  end

  it "should work for 1001" do
    expect(number_to_words(1001)).to eq("one thousand and one")
  end

  it "should work for 1234" do
    expect(number_to_words(1234)).to eq("one thousand two hundred and thirty-four")
  end

  it "should work for 10234" do
    expect(number_to_words(10234)).to eq("ten thousand two hundred and thirty-four")
  end

  it "should work for 50000" do
    expect(number_to_words(50000)).to eq("fifty thousand")
  end

  it "should work for 55234" do
    expect(number_to_words(55234)).to eq("fifty-five thousand two hundred and thirty-four")
  end

  it "should work for 500000" do
    expect(number_to_words(500000)).to eq("five hundred thousand")
  end

  it "should work for 987654" do
    expect(number_to_words(987654)).to eq("nine hundred and eighty-seven thousand six hundred and fifty-four")
  end

  it "should work for 999990" do
    expect(number_to_words(999990)).to eq("nine hundred and ninety-nine thousand nine hundred and ninety")
  end

  it "should work for 900001" do
    expect(number_to_words(900001)).to eq("nine hundred thousand and one")
  end

  it "should not work for -1" do
    expect(number_to_words(-1)).to eq("not in range")
  end

  it "should not work for 1000000" do
    expect(number_to_words(1000000)).to eq("not in range")
  end

end