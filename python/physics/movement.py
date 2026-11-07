class newtlaws:
  class fma:
    def fmtoa(f, m):
      return f/m

    def fatom(f, a):
       return f/a

    def amtof(a, m):
      return a*m

    #BIGBRAINFORMULA: F=ma
    
  class bounce:
    def bounce(f, ang, circdivby):
      halfc = circdivby/2
      return f, (0-((ang-halfc)%halfc))+halfc #"%halfc" Just in case the user forgot to do that in real application a an angle variable.
  class inertia:
    def inertia(a, ang):
      return a, ang

class translationmetrics:
  def adtot(a, d):
    return d/a
  def attod(a, t):
    return t/a
  def dttoa(d, t):
    return d/t
  
    #BIGBRAINFORMULA: d=t/a
