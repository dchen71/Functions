require_relative "../count_word"
require 'rspec'

describe CountWords do
  subject(:countwords) { CountWords.new('attg','at') }

  describe '#text' do
    it "should equal attg" do
      expect(countwords.text).to eq "attg"
    end
  end

  it 'has accessor for counts' do
    is_expected.to respond_to(:counts)
  end

  it "has accessor for text" do
    is_expected.to respond_to(:text) 
  end 
  it "has accessor for pat" do
    is_expected.to respond_to(:pat) 
  end

  it 'should initialize counts to 0' do
    expect(countwords.counts).to eq(0)
  end

  it "has method count_pat" do
    is_expected.to respond_to(:count_pat) 
  end

  context "values" do
    it "content attribute should have value 0" do
      expect(countwords.count_pat).to eq(1)
    end

    it 'count_pat should change counts' do
      countwords.count_pat
      expect(countwords.counts).to eq(1)
    end

    it 'case where pattern is not in string' do
      countwords.pat = 'cat'
      countwords.text = 'atgat'
      expect(countwords.count_pat).to eq(0)
    end

    it 'case where pattern is long' do
      countwords.pat = 'CCCCGTGCC'
      countwords.text = 'TGTACCCCGTGGATCCCCGTGCCCCCGTGTCCCCGTGGTAATAGTCTTCCCCCGTGCCCCGTGCTGCCGTCATCCCCGTGCCCCGTGGCCCCCGTGCCCCCCGTGCGACTAGGGATGCCCCGTGCCTCCCCGTGGCCCCGTGATACCCCGTGCCCCGTGCTGGGCCCCGTGATCTATTGACCCCCGTGCCCCCGTGCCCCGTGCCCCGTGGCCCCGTGCCCCGTGCCCCGTGCCCCGTGTCCCCGTGTCCCCCGTGGTACCGCTCGCCCCGTGGATATTGTCCCCGTGCCCCGTGCCCCCGTGCCCCGTGATGCCTCCCCCGTGCCCCGTGACCCCGTGTTTGACGCCCCGTGCCCCGTGTCCCCGTGCGCCCCGTGCCCCGTGGGAACATAGCCCCGTGCCCCCGTGGAAGCCTGTGTCCCCGTGCCCCCGTGAATCCCCGTGAGACCCCGTGTCCCCGTGGGCTCCCCGTGCCCCGTGACCCCGTGCCCCGTGCTCCCCCGTGCTCCCCGTGACCCCCGTGGCCCCGTGTCACGATGGCCCCGTGGGTAGCAAACATCCCCGTGCCCCGTGTCCCCCGTGACCCCGTGCCCCCGTGTTATCAGATCCCCGTGACCCCGTGCCCCGTGGCACCCCGTGCCCCCGTGCCCCGTGACCCCGTGCCCCCCGTGTCCCCGTGAAACTACCCCGTGCCCCGTGCCCCGTGCCCCGTGACCCCGTGTCCCCGTGTCCCCGTGAGTTGGTTGTCGACACACCTGCAACCCCCGTGAGCCCCGTGTGACCCCGTGAGCCCCGTGGACCCCGTGCCCCGTGCCCCGTGAGCCCCCGTGAACCCCGTGCCCCGTGATATTCCCCCGTGTGGCCCCGTGATCCCCGTGCGCCCCCGTGACCCCGTGACTGGGTCCCCCGTGCCCCGTGCCCCGTGTGTTGAGCCCCGTGATCTCCCCGTGCCCCGTG'
      expect(countwords.count_pat).to eq(30)
    end
  end

end