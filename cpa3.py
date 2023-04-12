class city:
      def __init__(self,city_id,state_name,city_name,covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds):
            self.city_id=city_id
            self.state_name=state_name
            self.city_name=city_name
            self.covidbeds=covidbeds
            self.avlblcovbeds=avlblcovbeds
            self.ventilbeds=ventilbeds
            self.avlblventilbeds=avlblventilbeds
            
class CovBedsAnalysis:
      def __init__(self,analysis_nam,city_list):
          self.analysis_nam=analysis_nam
          self.city_list=city_list

      def get_StateWiseAvlblBedStats(self, parameter_list):
            pass
          
              



if __name__=="__main__":
      pass
    