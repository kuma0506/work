package com.photo.domain.users;
// Generated 2021/03/10 5:31:48 by Hibernate Tools 5.3.9.Final


import javax.persistence.Column;
import javax.persistence.Embeddable;

/**
 * UsersAcountEntityId generated by hbm2java
 */
@Embeddable
public class UsersAcountEntityId  implements java.io.Serializable {


     private String usersId;
     private String usersPassword;

    public UsersAcountEntityId() {
    }

    public UsersAcountEntityId(String usersId, String usersPassword) {
       this.usersId = usersId;
       this.usersPassword = usersPassword;
    }
   


    @Column(name="users_id", nullable=false, length=4)
    public String getUsersId() {
        return this.usersId;
    }
    
    public void setUsersId(String usersId) {
        this.usersId = usersId;
    }


    @Column(name="users_password", nullable=false, length=8)
    public String getUsersPassword() {
        return this.usersPassword;
    }
    
    public void setUsersPassword(String usersPassword) {
        this.usersPassword = usersPassword;
    }


   public boolean equals(Object other) {
         if ( (this == other ) ) return true;
		 if ( (other == null ) ) return false;
		 if ( !(other instanceof UsersAcountEntityId) ) return false;
		 UsersAcountEntityId castOther = ( UsersAcountEntityId ) other; 
         
		 return ( (this.getUsersId()==castOther.getUsersId()) || ( this.getUsersId()!=null && castOther.getUsersId()!=null && this.getUsersId().equals(castOther.getUsersId()) ) )
 && ( (this.getUsersPassword()==castOther.getUsersPassword()) || ( this.getUsersPassword()!=null && castOther.getUsersPassword()!=null && this.getUsersPassword().equals(castOther.getUsersPassword()) ) );
   }
   
   public int hashCode() {
         int result = 17;
         
         result = 37 * result + ( getUsersId() == null ? 0 : this.getUsersId().hashCode() );
         result = 37 * result + ( getUsersPassword() == null ? 0 : this.getUsersPassword().hashCode() );
         return result;
   }   


}


