class Timer
  attr_accessor :seconds


  def initialize
    @seconds = 0
  end

  def time_string
    sec = @seconds % 60
    minutes = @seconds / 60 % 60
    hours = @seconds / 60 / 60

    sprintf("%02d:%02d:%02d", hours,minutes, sec)
  end

end