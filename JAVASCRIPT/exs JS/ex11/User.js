class User {
  constructor(fullname, email, password) {
    this.fullname = fullname
    this.email = email
    this.password = password
  }

  login(email, password) {
    if(this.email === email && this.password === password) {
    console.log('login relizado com sucesso!!')
    } else {
      console.log("falha ao fazer login! Email ou senha incorretos.")
    }
    
  }
}

const john = new User("John Doe", "john@gmail.com", "1234")

john.login("john@gmail.com", "1234")