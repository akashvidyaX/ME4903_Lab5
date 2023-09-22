def degrees_of_freedom(m, N, J, f1, f2, f3):
  """
  Calculates the number of degrees of freedom of a mechanism.

  Args:
    m: The number of degrees of freedom of a single body.
    N: The number of links in the system.
    J: The number of joints in the system.
    f1: The number of degrees of freedom of joint 1.
    f2: The number of degrees of freedom of joint 2.
    f3: The number of degrees of freedom of joint 3.

  Returns:
    The number of degrees of freedom of the mechanism.
  """

  return m * (N - 1 - J) + f1 + f2 + f3

def main():
  """
  Gets the input from the user and prints out the number of degrees of freedom.
  """

  m = int(input("Enter the number of degrees of freedom of a single link: "))
  N = int(input("Enter the number of links in the system: "))
  J = int(input("Enter the number of joints in the system: "))
  f1 = int(input("Enter the number of degrees of freedom of joint 1: "))
  f2 = int(input("Enter the number of degrees of freedom of joint 2: "))
  f3 = int(input("Enter the number of degrees of freedom of joint 3: "))

  dof = degrees_of_freedom(m, N, J, f1, f2, f3)
  print("The number of degrees of freedom is", dof)

if __name__ == "__main__":
  main()