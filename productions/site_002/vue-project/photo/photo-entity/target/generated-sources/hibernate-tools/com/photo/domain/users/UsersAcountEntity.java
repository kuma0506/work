package com.photo.domain.users;
// Generated 2021/03/10 5:31:48 by Hibernate Tools 5.3.9.Final


import com.photo.infra.jpa.BaseEntity;
import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

/**
 * UsersAcountEntity generated by hbm2java
 */
@Entity
@Table(name="users_acount"
)
public class UsersAcountEntity extends BaseEntity implements java.io.Serializable {


     private UsersAcountEntityId id;
     private String usersName;

    public UsersAcountEntity() {
    }

	
    public UsersAcountEntity(UsersAcountEntityId id) {
        this.id = id;
    }
    public UsersAcountEntity(UsersAcountEntityId id, String usersName) {
       this.id = id;
       this.usersName = usersName;
    }
   
     @EmbeddedId

    
    @AttributeOverrides( {
        @AttributeOverride(name="usersId", column=@Column(name="users_id", nullable=false, length=4) ), 
        @AttributeOverride(name="usersPassword", column=@Column(name="users_password", nullable=false, length=8) ) } )
    public UsersAcountEntityId getId() {
        return this.id;
    }
    
    public void setId(UsersAcountEntityId id) {
        this.id = id;
    }

    
    @Column(name="users_name", length=100)
    public String getUsersName() {
        return this.usersName;
    }
    
    public void setUsersName(String usersName) {
        this.usersName = usersName;
    }




}


