# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
print ("");
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9;
  return c_temp;

def c_to_f(c_temp):
  f_temp=(c_temp*9/5)+32;
  return f_temp;

print ("f100_temp 100");
f100_in_celcius = f_to_c(100)
print(f100_in_celcius);
print("f100 in celcius is " + str(f100_in_celcius));

print ("");

print("c0 in celcius is 0");
c0_in_fahrenheit=c_to_f(0)
print (c0_in_fahrenheit);
print ("c0 in fahrenheit is " + str(c0_in_fahrenheit));

print ("");

print ("train_mass = 22680, train_acceleration = 10, train_distance = 100, bomb_mass = 1")

print ("");

def get_force(mass,acceleration):
  force=mass*acceleration
  return force

force=get_force(train_mass, train_acceleration);
print (force);
train_force=str(force)

print ("The GE train supplies " + train_force + " Newtons of force")

c=3*10**8
def get_energy(mass,c):
  energy=mass*c**2
  return energy

bomb_energy=get_energy(bomb_mass,c)
print (bomb_energy);

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules");

def get_work(mass,acceleration,distance):
  force=get_force(mass,acceleration)
  work=force*distance
  return work;

train_work=get_work(train_mass,train_acceleration,train_distance)
print (train_work);
print ("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters");
