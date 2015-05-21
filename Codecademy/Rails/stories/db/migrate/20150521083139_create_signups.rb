class CreateSignups < ActiveRecord::Migration
  def change
    create_table :signups do |t|
      t.string :firstname
      t.string :email

      t.timestamps null: false
    end
  end
end
