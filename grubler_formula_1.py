def degrees_of_freedom(m, N, J, f1, f2, f3):
  """
  Calculates the number of degrees of freedom of a mechanism.

  Args:
    m: The number of degrees of freedom of a single body.
    N: The number of links in the system.
    J: The number of joints in the system.
    f1: The number of joints with 1 degree of freedom.
    f2: The number of joints with 2 degree of freedom.
    f3: The number of joints with 3 degree of freedom.

  Returns:
    dof: The number of degrees of freedom of the mechanism.
  """

  return m * (N - 1 - J) + f1 + (2 * f2) + (3 * f3)

def main():
  """
  Gets the input from the user and prints out the number of degrees of freedom.
  """

  m = int(input("Enter the number of degrees of freedom of a single link: "))
  N = int(input("Enter the number of links in the system: "))
  J = int(input("Enter the number of joints in the system: "))
  f1 = int(input("Enter the number of joints that have 1 degree of freedom: "))
  f2 = int(input("Enter the number of joints that have 2 degree of freedom: "))
  f3 = int(input("Enter the number of joints that have 3 degrees of freedom: "))

  dof = degrees_of_freedom(m, N, J, f1, f2, f3)
  print("The number of degrees of freedom is", dof)

if __name__ == "__main__":
  main()
