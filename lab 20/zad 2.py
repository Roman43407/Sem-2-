class Bmr:

    def w_ppm(sel, weight, height, age):
        return 665.1 + (9.6 * weight) + (1.85 * height) - (4.7 * age)

    def m_ppm(self, weight, height, age):
        return 66.5 + (13.75 * weight) + (5 * height) - (6.8 * age)



if __name__ == '__main__':
    bmr = Bmr()
    print(bmr.m_ppm(85 ,175, 18))


