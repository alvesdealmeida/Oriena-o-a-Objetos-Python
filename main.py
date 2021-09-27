from fracao import Fracao

f = Fracao(15,45)
g = Fracao(50,75)

print("f = 15/45 = %s" % f)
print("g = 50/75 = %s" % g)
print("f + g = %s" % (f + g))
h = Fracao(10,28)
print("h = 10/28 = %s" % h)
print("f * h = %s"  % (f*h))
print("f + g + h = %s" % (f + g + h))
print("f + g * h = %s" % (f + g * h))
print("g - f - f = %s" % (g - f - f))
print("f * 2 = %s" % (f * 2))
print("f + 2 = %s" % (f + 2))
print("f / g = %s" % (f / g))
f += g * 2
print("f += g * 2 = %s" %  f)
f -= g * 2
print("f -= g * 2 = %s" % f)

try:
	print("2 + f =")
	print(2 + f)
except (ValueError, TypeError) as e:
	print("Exception caught: %s" %e)
	print("f == h % " % (f==h))
	print("f=g=h")
	f=g=h
	print("f == h %s" % (f==h))
try:
	print("f += \ 'a\'")
	f += "a"
except(ValueError, TypeError) as e:
	print("Exception caught: %s" % e)


try:
	print("Fracao(2,0) = ")
	print(Fracao(2,0))
except(ValueError, TypeError) as e:
	print("Exception caught: %s" % e)
try:
	print("Fracao(5,3) / Fracao(0,4)")
	print(Fracao(5,3) / Fracao(0,4))
except Exception as e:
	print("Exception caught: %s" % e)

if __name__=="__main__":
			sys.exit(main())












