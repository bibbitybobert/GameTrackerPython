export class user{
	id: string;
	fName: string;
	lName: string;
	email: string;
	passwordHash: string;

	constructor(id: string, fName: string, lName: string, email:string, passwordHash: string) {
		this.id = id;
		this.fName = fName;
		this.lName = lName;
		this.email = email;
		this.passwordHash = passwordHash;
	}
}