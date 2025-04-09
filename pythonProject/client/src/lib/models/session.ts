export class session {
	id: string;
	userId: string;
	expiresAt: Date;

	public constructor(id: string, userId: string, expiresAt: Date) {
		this.id = id;
		this.userId = userId;
		this.expiresAt = expiresAt;
	}
}