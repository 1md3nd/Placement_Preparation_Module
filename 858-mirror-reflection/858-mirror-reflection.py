import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
         # incident_angle = int(round(math.degrees(math.atan2(p,q))))
            p = 2 q = 1
            incident_angle = reflected_angel -> their normal is same so the point hit by ray after reff. 
            temp = 2*q -> 2
            and p == temp -> it is on recptor on opp wall (west)
            if temp > p -> then the ray hits north wall
                then p = p - q and q = p * math.tan(incident_angle)
            
            
        """
        # wall = p
        # count = 0
        # try:
        #     while wall != q:
        #         incident_angle = int(round(math.degrees(math.atan2(p,q))))
        #         print(incident_angle)
        #         p = wall - q
        #         q = p * math.tan(incident_angle)
        #         print(p,q)
        #         count += 1
        # except:
        #     print(count)
        lcm = p * q // gcd(p,q)
        box = lcm // p
        if box % 2 == 0:
            return 0
        if (lcm // q) % 2  == 0:
            return 2
        return 1