class TagManipulator():
  def parse_string(self, tags):

        #regex = ",\\ *"
        #result = re.split(regex, tags)

        if len(tags) < 1 or tags == "," :
          result = []
        else:
          result = [tags]
        
        
        return result

