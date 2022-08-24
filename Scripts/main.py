if __name__ == '__main__':
  from utils import *
  position = sys.argv[1]
  year = sys.argv[2]
  week = sys.argv[3]
  pull(position,year,week)
  teamyear = sys.argv[4]
  teamweek = sys.argv[5]
  teamnamepull(teamyear,teamweek)
  file1 = sys.argv[6]
  file2 = sys.argv[7]
  teamcorrection(file1,file2)
