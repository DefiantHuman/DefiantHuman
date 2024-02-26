using System;

class MainClass {
  public static void Main (string[] args) {
    string userName = "gcimoch";
    string userPass = "Wordpass!";
    Login(userName, userPass);
  }
  static void Login(string userName,  string userPass){
    Console.Clear();
    Console.WriteLine("Login:");
userFail:
    Console.Write("Username: ");
    string loginName = Console.ReadLine();
    if (loginName == userName){
passFail:
      Console.Write("Password: ");
      string loginPass = Console.ReadLine();
      if (loginPass == userPass){
        Mainloop();
      }
      else if (loginPass == "Exit"){}
      else {Console.WriteLine("Ivalid Password");goto passFail;}
    }
    else if (loginName == "Exit"){}
    else {Console.WriteLine("User not found.");goto userFail;}
  }
  static void Mainloop(){
    string i = "";
    Console.Clear();
    Console.WriteLine("Welcome");
Main:
    Console.Write("-> ");
    i = Console.ReadLine();
    if (i == "Calc"){
        Calc();
    }
    else if (i == "Average"){
        Average();
    }
    else if (i == "?"){
        Console.WriteLine("Options: Calc, Average, Exit, ?");
        goto Main;
    }
    else if (i == "Exit"){}
    else{
        Mainloop();
    }
  }
  static void Calc(){
        Console.Clear();
        Console.Write("Num 1: ");
        double Num1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Num 2: ");
        double Num2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine(Num1 + Num2);
        Console.WriteLine("Enter to exit");
        Console.ReadLine();
        Mainloop();
  }
  static void Average(){
        Console.Clear();
        Console.Write("Num 1: ");
        double Num1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Num 2: ");
        double Num2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine((Num1 + Num2) / 2);
        Console.WriteLine("Enter to exit");
        Console.ReadLine();
        Mainloop();
  }
}