import math

class PointND:
    def __init__(self, *args):
        for item in args:
            if not type(item) == float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t=args
        self.n=len(args)

    def __str__(self):
        string="("
        for item in self.t:
            string+=format(item, '.2f')+", "
        string=string.rstrip(", ")
        string+=")"
        return string

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if not other.n == self.n:
            raise ValueError("Cannot calculate distance between points of difference cardinality.")
        distance=math.sqrt(sum([(i-j)**2 for i,j in zip(self.t,other.t)]))
        return distance

    def nearestPoint(self,points):
        if not points:
            raise ValueError("Input cannot be empty")
        min_val=9999999999
        n_point=points[0]
        for point in points:
            if self.distanceFrom(point) < min_val:
                min_val=self.distanceFrom(point)
                n_point = point
        return n_point

    def clone(self):
        return PointND(*self.t)

    def __add__(self,other):
        if type(other) == float:
            return PointND(*tuple(i+other for i in self.t))
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(i+j for i,j in zip(self.t,other.t)))

    __radd__=__add__


    def __sub__(self, other):
        if type(other) == float:
            return PointND(*tuple(i-other for i in self.t))
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(i-j for i,j in zip(self.t,other.t)))

    def __mul__(self, other):
        return PointND(*tuple(i*other for i in self.t))

    __rmul__=__mul__

    def __truediv__(self, other):
        return PointND(*tuple(i/other for i in self.t))

    def __neg__(self):
        return PointND(*tuple(-i for i in self.t))

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return all([i==j for i,j in zip(self.t,other.t)])

    def __ne__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return all([i!=j for i,j in zip(self.t,other.t)])

    def __gt__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.distanceFrom(PointND(*[0.0]*self.n)) > other.distanceFrom(PointND(*[0.0]*other.n))

    def __ge__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.distanceFrom(PointND(*[0.0]*self.n)) >= other.distanceFrom(PointND(*[0.0]*other.n))

    def __lt__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.distanceFrom(PointND(*[0.0]*self.n)) < other.distanceFrom(PointND(*[0.0]*other.n))

    def __le__(self, other):
        if not self.n == other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.distanceFrom(PointND(*[0.0]*self.n)) <= other.distanceFrom(PointND(*[0.0]*other.n))

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        PointND.__init__(self,x,y,z)
        self.x=x
        self.y=y
        self.z=z

class PointSet:
    def __init__(self, **kwargs):
        if not kwargs:
            self.points=set()
            self.n=0
        elif "pointList" not in kwargs:
            raise KeyError("'pointList' input parameter not found")
        elif not kwargs["pointList"]:
            raise ValueError("'pointList' input parameter cannot be empty")
        else:
            self.points=set()
            self.n=kwargs["pointList"][0].n
            for point in kwargs["pointList"]:
                self.addPoint(point)

    def addPoint(self,p):
        if p.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        else:
            self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        minPoint=[9999999]*self.n
        maxPoint=[0]*self.n
        for point in self.points:
            i=0
            while i < self.n:
                if point.t[i] < minPoint[i]:
                    minPoint[i]=point.t[i]
                if point.t[i] > maxPoint[i]:
                    maxPoint[i]=point.t[i]
                i+=1
        return (PointND(*minPoint),PointND(*maxPoint))

    def computeNearestNeighbors(self,otherPointSet):
        n=[]
        for point in self.points:
            n.append((point,point.nearestPoint(list(otherPointSet.points))))
        return n

    def __add__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        else:
            self.points.add(other)
        return self

    def __sub__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        elif other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self, other):
        if other in self.points:
            return True
        else:
            return False









if __name__ == '__main__':
    pass