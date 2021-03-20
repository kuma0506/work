package com.photo.domain.persion;
// Generated 2021/03/10 5:31:48 by Hibernate Tools 5.3.9.Final


import javax.persistence.Column;
import javax.persistence.Embeddable;

/**
 * PersonRelationEntityId generated by hbm2java
 */
@Embeddable
public class PersonRelationEntityId  implements java.io.Serializable {


     private int selfId;
     private int otherId;

    public PersonRelationEntityId() {
    }

    public PersonRelationEntityId(int selfId, int otherId) {
       this.selfId = selfId;
       this.otherId = otherId;
    }
   


    @Column(name="self_id", nullable=false)
    public int getSelfId() {
        return this.selfId;
    }
    
    public void setSelfId(int selfId) {
        this.selfId = selfId;
    }


    @Column(name="other_id", nullable=false)
    public int getOtherId() {
        return this.otherId;
    }
    
    public void setOtherId(int otherId) {
        this.otherId = otherId;
    }


   public boolean equals(Object other) {
         if ( (this == other ) ) return true;
		 if ( (other == null ) ) return false;
		 if ( !(other instanceof PersonRelationEntityId) ) return false;
		 PersonRelationEntityId castOther = ( PersonRelationEntityId ) other; 
         
		 return (this.getSelfId()==castOther.getSelfId())
 && (this.getOtherId()==castOther.getOtherId());
   }
   
   public int hashCode() {
         int result = 17;
         
         result = 37 * result + this.getSelfId();
         result = 37 * result + this.getOtherId();
         return result;
   }   


}


